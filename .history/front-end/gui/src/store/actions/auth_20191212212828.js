import * as actionTypes from "../actionTypes";
import axios from "axios";

import * as constants from "./../../../Data/constants";

export const authStart = () => {
  return {
    type: actionTypes.AUTH_START
  };
}

export const authSuccess = (response_data) => {
  return {
    type: actionTypes.AUTH_SUCCESS,
    props: response_data
  }
}

export const authFail = (error) => {
  return {
    type: actionTypes.AUTH_ERROR,
    error: error
  }
}

export const authLogout = () => {
  const themeInfo = localStorage.getItem(constants.THEME_CONTROLLER);
  localStorage.clear();
  localStorage.setItem(constants.THEME_CONTROLLER, themeInfo);
  
  return {
    type: actionTypes.AUTH_LOGOUT
  }
}


export const checkAuthTimeout = (expirationDate) => {
  return dispatch => {
    setTimeout(() => {
      dispatch(authLogout())
    }, 300000 * 1000);
  }
}
export const auth = (email, password, history, authFailCB, prevPage) => {
  return dispatch => {
    // dispatch(authStart());
    // dispatch(authLogout());
    const loginData = {
      email: email,
      password: password
    }


    axios.post(`/api/users/org_users/login`, loginData)
      .then(response => {
        axios.defaults.headers.common['Authorization'] = "JWT " + response.data.token;
        if(!prevPage){
          axios.get(`/api/apps/`).then(data => {
            if ( data.data.data && data.data.data.length !== 0) {
              if(window.location.pathname === '/org/login' || window.location.pathname === '/org/' || window.location.pathname === '/org')
                history.push("/dashboard");
            } else {
              history.push("/workflows/add");
            }
          }).catch(err => {
            console.log(err.response.data.message);
          })
        }
        
        let expirationDate = new Date(0); // The 0 there is the key, which sets the date to the epoch
        expirationDate.setUTCSeconds(response.data.token_expiration);
        
        localStorage.setItem("token", response.data.token);
        localStorage.setItem("username", response.data.first_name);
        localStorage.setItem("expirationDate", expirationDate);
        localStorage.setItem("email", response.data.data.id);
        localStorage.setItem("userId", response.data.data.id);


        let response_data = {
          'token': response.data.token,
          'username': response.data.data.email,
          'id': response.data.data.id,
          'groupId': response.data.data.roles[0].id,
          'groupName': response.data.data.roles[0].name,
          'firstName': response.data.data.first_name,
          'lastName': response.data.data.last_name,
          'employeeId': response.data.data.employee_id,  
          'uiPermissions': response.data.data.ui_permissions,
          'manager': response.data.data.manager   
        }
        dispatch(authSuccess(response_data));
        dispatch(checkAuthTimeout(response.data.token_expiration));
      })
      .catch(err => {
        authFailCB(err.response.data.message)
        // dispatch(authFail(err.response.data.message));
      });
  }
}


export const authCheckState = (CB) => {
  return dispatch => {
    const token = localStorage.getItem('token');
    const userId = localStorage.getItem('userId');
    if (!token) {
      dispatch(authLogout());
      CB()
    } else {
      const expirationDate = new Date(localStorage.getItem('expirationDate'));
      if (expirationDate <= new Date()) {
        dispatch(authLogout());
        CB()
      } else {
        axios.defaults.headers.common['Authorization'] = "JWT " + token;
        axios.get('/api/users/org_users/' + userId).then(response=>{
          let response_data = {
            'token': token,
            'username': response.data.data.email,
            'id': response.data.data.id,
            'groupId': response.data.data.roles[0].id,
            'groupName': response.data.data.roles[0].name,
            'firstName': response.data.data.first_name,
            'lastName': response.data.data.last_name,  
            'employeeId': response.data.data.employee_id,
            'uiPermissions': response.data.data.ui_permissions,
            'manager' : response.data.data.manager
          }

          dispatch(authSuccess(response_data))
          CB()
        })
        .catch(err  => {
          dispatch(checkAuthTimeout((expirationDate.getTime() - new Date().getTime()) / 1000));
          CB()
        })

      }
    }
  };
};

