import React, { useEffect } from 'react'
import "../styles/Logout.css";
import { useNavigate } from 'react-router-dom';
import { toast } from "react-toastify";

const Logout = () => {

    const navigate = useNavigate();
    
    useEffect(() => {

        localStorage.removeItem("auth");
        console.log(JSON.parse(localStorage.getItem("logout","auth")));
        toast.error("Logout Successful");
        navigate("/login");
        // setTimeout(() => {
        //     navigate("/");
        // }, 3000);
    }, []);

  // return (
  //   <div className='logout-main'>
  //   <h1>Logout Successful!</h1>
  //   <p>You will be redirected to the landing page in 3 seconds...</p>
  // </div>
  // )
}

export default Logout