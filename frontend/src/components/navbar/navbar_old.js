import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import "./navbar.css"
import "../../index.css"
import Logo from "../../assets/logo.png"
const Navbar = () => {
    return (
        <nav class="navbar navbar-expand-lg bg-body-tertiary color" >
        <div class="container-fluid" style={{width : '100%'}}>
          <a class="navbar-brand" href="#" style={{width : '12%'}}><img style={{width : '55%',marginLeft:'25%'}} src={Logo}></img></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle font-all white-font small-font upper-font" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Diamond
                  </a>
                  <ul class="dropdown-menu color">
                    <li><a class="dropdown-item " href="#">Natural Diamond</a></li>
                    <li><a class="dropdown-item " href="#">Lab Created Diamond</a></li>
                    <li><a class="dropdown-item " href="#">Fancy Coloured Natural Diamond</a></li>
                    <li><a class="dropdown-item " href="#">Fancy Coloured Lab Diamond</a></li>
                    <li><hr class="dropdown-divider"/></li>
                    <li><a class="dropdown-item " href="#">Something else here</a></li>
                  </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link font-all white-font small-font upper-font" href="#">Jewellery</a>
              </li>
              <li class="nav-item">
                <a class="nav-link font-all white-font small-font upper-font" aria-current="page" href="#">Engagement Rings</a>
              </li>
              <li class="nav-item">
                <a class="nav-link font-all white-font small-font upper-font" aria-current="page" href="#">Wedding Rings</a>
              </li>
              <li class="nav-item">
                <a class="nav-link font-all white-font small-font upper-font" aria-current="page" href="#">Fine Jewellery</a>
              </li>
              
            </ul>
            {/* <form class="d-flex" role="search">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
              <button class="btn btn-outline-success white-font" type="submit">Search</button>
            </form> */}
          </div>
        </div>
      </nav>
    )
}

export default Navbar