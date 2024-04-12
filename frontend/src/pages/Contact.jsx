// require("dotenv").config();
import React, { useEffect, useState } from "react";
import Logo from "../assets/logo.png";
import { FaEye } from "react-icons/fa6";
import { FaEyeSlash } from "react-icons/fa6";
import "../styles/Login.css";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";
import Navbar1 from "../components/navbar/navbar";
// import { GoogleLogin } from '@react-oauth/google';

const client_id = "570396790642-osca4dukk6r09vlc77e0j7cdtvt9aruc.apps.googleusercontent.com"

const Contact = () => {
  const initialData = {
    name: "",
    email: "",
    message : ""
  }
  const [data, setData] = useState(initialData);
  const [ token, setToken ] = useState(JSON.parse(localStorage.getItem("auth")) || "");
  const navigate = useNavigate();



  const handleLoginSubmit = (e) => {
    e.preventDefault();
    console.log(e, data);
    e.target.reset(); 
    setData(initialData);
    toast.success("Thank you for reaching us....");
  };

  const handleChange = (e) => {
    e.preventDefault();
    setData(prev => ({
        ...prev, ...{[e.target.name] : e.target.value}
    }))
  };

  useEffect(() => {
    // fetchLuckyNumber();
    if(token == ""){
      navigate("/login");
      // toast.warn("Please login first to access dashboard");
    }
  }, [token]);


  return (
    <>
    <Navbar1/>
    <div className="login-main">
      <div className="login-right">
        <div className="login-right-container">
          <div className="login-center">
            <h2>Contact Us</h2>
            <p>Please enter your details</p>
            <form onSubmit={handleLoginSubmit} method="post">
              <input type="text" placeholder="Name" name="name" onChange={handleChange} />
              <input type="email" placeholder="Email" name="email"  onChange={handleChange}/>
              <input type="text" placeholder="Message" name="message" onChange={handleChange}/>

              <div className="login-center-buttons">
                <button type="submit">Submit</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    </>
  );
};

export default Contact;
