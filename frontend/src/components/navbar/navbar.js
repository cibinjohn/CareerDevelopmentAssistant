import React, { useState } from 'react';
import { Link, useNavigate } from "react-router-dom";
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import "@fortawesome/fontawesome-free/css/all.min.css";
import {
  MDBContainer,
  MDBNavbar,
  MDBNavbarBrand,
  MDBNavbarToggler,
  MDBIcon,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBNavbarLink,
  MDBBtn,
  MDBDropdown,
  MDBDropdownToggle,
  MDBDropdownMenu,
  MDBDropdownItem,
  MDBCollapse,
} from 'mdb-react-ui-kit';
import Logo from "../../assets/logo.png"
import "../../index.css"


export default function App() {
  const [openBasic, setOpenBasic] = useState(false);

  return (
    <MDBNavbar expand='lg' className='color' fixed='top' light bgColor='light'>
      <MDBContainer fluid>
        <MDBNavbarBrand href='/'>
        <img
              src={Logo}
              height='60'
              alt=''
              loading='lazy'
            />
            {/* <label>Career Compass</label> */}
        </MDBNavbarBrand>

        <MDBNavbarToggler
          aria-controls='navbarSupportedContent'
          aria-expanded='false'
          aria-label='Toggle navigation'
          onClick={() => setOpenBasic(!openBasic)}
        >
          <MDBIcon icon='bars' fas />
        </MDBNavbarToggler>

        <MDBCollapse navbar open={openBasic}>
          <MDBNavbarNav className='mr-auto mb-2 mb-lg-0'>
          

            {/* <MDBNavbarItem>
              <MDBDropdown>
                <MDBDropdownToggle tag='a' active aria-current='page'  className='nav-link white-font' role='button'>
                Diamond
                </MDBDropdownToggle>
                <MDBDropdownMenu>
                  <MDBDropdownItem className='white-font' link>Natural Diamond</MDBDropdownItem>
                  <MDBDropdownItem className='white-font' link>Lab Created Diamond</MDBDropdownItem>
                  <MDBDropdownItem className='white-font' link>Fancy Coloured Natural Diamond</MDBDropdownItem>
                  <MDBDropdownItem className='white-font' link>Fancy Coloured Lab Diamond</MDBDropdownItem>
                </MDBDropdownMenu>
              </MDBDropdown>
            </MDBNavbarItem> */}

            <MDBNavbarItem>
              <MDBNavbarLink className='white-font' href='/'>Home</MDBNavbarLink>
            </MDBNavbarItem>
            

            {/* <MDBNavbarItem>
              <MDBNavbarLink className='white-font' href='#'>Chat</MDBNavbarLink>
            </MDBNavbarItem> */}
            
            {/* <MDBNavbarItem>
              <MDBNavbarLink className='white-font' href='#'>About Us</MDBNavbarLink>
            </MDBNavbarItem> */}

            <MDBNavbarItem>
              <MDBNavbarLink className='white-font' href='/contact' >Contact Us</MDBNavbarLink>
            </MDBNavbarItem>

            {/* <MDBNavbarItem>
              <MDBNavbarLink className='white-font' href='#'>Fine Jewellery</MDBNavbarLink>
            </MDBNavbarItem> */}

            
          </MDBNavbarNav>

          {/* <MDBNavbarItem  className='d-flex'>
              <MDBNavbarLink  disabled href='#' tabIndex={-1}  className='white-font'>
                 Link
              </MDBNavbarLink>
            </MDBNavbarItem> */}

            <MDBNavbarItem  className='d-flex'>
            {/* <button to="/logout" className="logout-button">Logout</button> */}
            <span>
            <Link to="/Logout"><MDBIcon  className='white-font'  fas icon='right-from-bracket'></MDBIcon></Link>
                
              </span>
            </MDBNavbarItem>

          {/* <form className='d-flex input-group w-auto'>
            <input type='search' className='form-control' placeholder='Type query' aria-label='Search' />
            <MDBBtn color='primary'>Search</MDBBtn>
          </form> */}
        </MDBCollapse>
      </MDBContainer>
    </MDBNavbar>
  );
}