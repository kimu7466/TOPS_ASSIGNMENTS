const initialState = {
    email: '',
    password: '',
    retypePassword: '',
    firstName: '',
    lastName: '',
    phoneNumber: '',
    address: '',
    town: '',
    region: '',
    postcode: '',
    country: 'United Kingdom',
  };
  
  const formReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'SET_FIELD':
        return {
          ...state,
          [action.payload.field]: action.payload.value,
        };
      default:
        return state;
    }
  };
  
  export default formReducer;
  