// require("dotenv").config();
import React, { useEffect, useState } from "react";
import Logo from "../assets/logo.png";
import { FaEye } from "react-icons/fa6";
import { FaEyeSlash } from "react-icons/fa6";
import "../styles/Login.css";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";
// import { GoogleLogin } from '@react-oauth/google';

// const client_id = "570396790642-osca4dukk6r09vlc77e0j7cdtvt9aruc.apps.googleusercontent.com"

const Login = () => {
  const [showPassword, setShowPassword] = useState(false);
  const [ token, setToken ] = useState(JSON.parse(localStorage.getItem("auth")) || "False");
  const navigate = useNavigate();

  console.log("login token", token)

  const handleLoginSubmit = async (e) => {
    e.preventDefault();
    let email = e.target.email.value;
    let password = e.target.password.value;

    if (email.length > 0 && password.length > 0) {
      const formData = {
        mailid:email,
        password,
      };
      try {
        const response = await axios.put(
          "http://0.0.0.0:6999/credentials/validate",
          formData
        );
        console.log("responese token",response.data);
        console.log(typeof response.data.results.is_account_present);
        localStorage.setItem('auth', JSON.stringify(response.data.results.is_account_present));
        localStorage.setItem('email', JSON.stringify(response.data.results.credentials.mailid));
        const newtoken = JSON.parse(localStorage.getItem("auth"));
        if(newtoken == "True"){
          toast.success("Login successfull");
          navigate("/");
        }else{
          toast.error("User Not Authenticated");
          navigate("/login");
        }
        
      } catch (err) {
        console.log(err);
        navigate("/login");
        toast.error("User Not Authenticated");
        e.target.reset();
      }
    } else {
      navigate("/login");
      toast.error("Please fill all inputs");
      e.target.reset();
    }
  };

  // useEffect(() => {
  //   console.log("login token", token);
  //   if(token == "False"){
  //     toast.success("Please Logins In-->");
  //     navigate("/login");
  //   }
  // }, []);

useEffect(() => {
    console.log("login token", token);
    if(token == "True"){
      // toast.success("Please Logins In-->");
      navigate("/");
    }else{
      navigate("/login");
    }
  }, []);
  
  return (
    <div className="login-main">
      <div className="login-right">
        <div className="login-right-container">
          <div className="login-logo">
            <img src={Logo} alt="" />
          </div>
          <div className="login-center">
            <h2>Welcome back!</h2>
            <p>Please enter your details</p>
            <form onSubmit={handleLoginSubmit}>
              <input type="email" placeholder="Email" name="email" />
              <div className="pass-input-div">
                <input
                  type={showPassword ? "text" : "password"}
                  placeholder="Password"
                  name="password"
                />
                {showPassword ? (
                  <FaEyeSlash
                    onClick={() => {
                      setShowPassword(!showPassword);
                    }}
                  />
                ) : (
                  <FaEye
                    onClick={() => {
                      setShowPassword(!showPassword);
                    }}
                  />
                )}
              </div>

              <div className="login-center-options">
                <div className="remember-div">
                  <input type="checkbox" id="remember-checkbox" />
                  <label htmlFor="remember-checkbox">
                    Remember for 30 days
                  </label>
                </div>
                {/* <a href="#" className="forgot-pass-link">
                  Forgot password?
                </a> */}
              </div>
              <div className="login-center-buttons">
                <button type="submit">Log In</button>
                {/* <button type="submit">
                  <img src={GoogleSvg} alt="" />
                  Log In with Google
                </button> */}
                {/* <GoogleLogin
                  onSuccess={credentialResponse => {
                    console.log(credentialResponse);
                  }}
                  onError={() => {
                    console.log('Login Failed');
                  }}
                />; */}
              </div>
            </form>
          </div>

          <p className="login-bottom-p">
            Don't have an account? <Link to="/register">Sign Up</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
