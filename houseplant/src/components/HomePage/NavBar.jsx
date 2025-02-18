import React from 'react'
import './NavBar.css'
import mainLogo from "../../logos (1)/GreenPlantsEverywhere.png"
import mainHeader from "../../logos (1)/GPE_T_cropped.png"
function NavBar() {
  return (
    
    <nav className='navbar'>
      <div className='navbar-left'>
        <img src ={mainLogo} className = "logo"/>
      </div>
      <div className='navbar-center'>
          <img src = {mainHeader} class = "navbar-logo" alt="greenplantseverywherelogo"/>
      </div>
    </nav>
  )
}

export default NavBar;