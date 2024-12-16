import React, { useEffect, useState } from 'react'
import ReactDOM from "react-dom";
import "../styles/Dashboard.css";
import { Link, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import axios from 'axios';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Navbar1 from "../components/navbar/navbar";
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';




const Premium = () => {
  const [ token, setToken ] = useState(JSON.parse(localStorage.getItem("auth")) || "");
  const [ email, setEmail ] = useState(JSON.parse(localStorage.getItem("email")) || "false");
  const [ loading, setLoading ] = useState(false);
  const [ data, setData ] = useState({});
  const navigate = useNavigate();



  
  useEffect(() => {
    // fetchLuckyNumber();
    if(token === ""){
      navigate("/login");
      toast.warn("Please login first to access dashboard");
    }
  }, [token]);

  const MessageWithAccordion = ({ sender, message }) => {
    return (
      (sender === "user" ?
      <p className={`chat-bubble ${sender}-bubble`}>
        <strong style={{color:"#fff"}}>You : </strong> {message}
      </p>:
      (
        <Accordion style={{maxWidth:"80%", padding:"0",margin:0, borderRadius:"10px"}} className='chat-bubble'>
        <AccordionSummary style={{margin:"0 auto", marginTop: "5px"}}
          expandIcon={<ExpandMoreIcon />} 
          aria-controls="panel1-content"
          id="panel1-header" 
        >
          <Typography><strong style={{color:"#007bff"}}>Bot : </strong> {message.answer}</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>{message.matching_docs.map((doc, index) => (
            <>
            <div key={index}>{doc}</div>
            <br/>
            </>
          ))}</Typography>  
        </AccordionDetails>
      </Accordion>
      ) 
      )
    );
  };
  
  const appendMessage = async (sender, message) => {
    const chatContainer = document.getElementById("output");
    const messageContainer = document.createElement('div');
    ReactDOM.render(
      <MessageWithAccordion sender={sender} message={message} />,
      messageContainer
    );
    chatContainer.appendChild(messageContainer);
    chatContainer.scrollTop = chatContainer.scrollHeight;
  };

  const AppendData = async (event) => {
    setLoading(true);
    event.preventDefault();
    console.log(email);
    const formData = new FormData(event.target);
    const query = event.target.prompt.value;
    const formData1 = {
      mailid: email,
      query
    };

    const response = await axios.put("http://0.0.0.0:6999/chat/premium/response", formData1);
    const userInput = formData.get("prompt");

    // // Dummy response until your model is ready
    // const dummyResponse = response.data.results.answer || 
    //   "This is a dummy response which will be replaced with actual response.";

    // Append user message to chat
    appendMessage("user", userInput);

    // Simulate delay before bot response
    setTimeout(function () {
      setLoading(false);
      appendMessage("bot", response.data.results);
    }, 5000);

    document.getElementById("prompt").value = "";
  }



  // const appendMessage = async (sender, message) => {
  //   const chatContainer = document.getElementById("output");
  //   const newMessage = document.createElement("p");
  //   newMessage.className = "chat-bubble " + sender + "-bubble";
  //   newMessage.innerHTML = sender === "user" ?  
  //     "<strong style='color:#fff'>" +
  //     "You" + 
  //     ":</strong> " +
  //     message
  //     :
  //     "<strong>" +
  //     "Bot" +
  //     ":</strong> " +
  //     message.answer;
  //   chatContainer.appendChild(newMessage);
  //   chatContainer.scrollTop = chatContainer.scrollHeight;
  // }

  const handleClick = () => {
    navigate("/");
  } 

  // const AppendData = async (event) => {
  //   event.preventDefault();
  //   const formData = new FormData(event.target);
  //   const query = event.target.prompt.value;
  //   const formData1 = {
  //     query
  //   };
  //   console.log(query);

  //   const response = await axios.put("http://0.0.0.0:6999/chat/response", formData1);




  //   const userInput = formData.get("prompt");


  //   // Append user message to chat
  //   appendMessage("user", userInput);

  //   // Simulate delay before bot response
  //   setTimeout(function () {
  //     // Append bot response to chat
  //     appendMessage("bot", response.data.results);
  //   }, 1000);

  //   // Clear input field after sending message
  //   document.getElementById("prompt").value = "";
  // }

  

  // const toggle = async () => {
  //   document.body.classList.toggle("dark-mode");
  // }


  return (
    <div style={{overflow:"auto"}}>
      <Navbar1/>

      <div id="chat-container" style={{}}>
      <h1>Career Compass</h1>
      <div id="output"></div>
      <form id="userForm" onSubmit={AppendData}>
        <input
          type="text"
          id="prompt"
          name="prompt"
          placeholder="Type your message here..."
          required
        />
        <input style={{marginBottom: "16px"}} type="submit" value="Send"  disabled={loading}/>
        <input style={{marginBottom: "16px", marginLeft:"10px"}} type="button" onClick={handleClick} value="Select Beta model" />
      </form>
      {/* <div class="toggle-container">
        <span class="toggle-label">Dark Mode:</span>
        <label class="toggle">
          <input type="checkbox" class="toggle-input" id="darkModeToggle" onClick={toggle}/>
          <span class="toggle-handle"></span>
        </label>
      </div> */}
    </div>



    </div>
  )
}

export default Premium
