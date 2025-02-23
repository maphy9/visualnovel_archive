import React, { useState } from 'react'
import { Outlet } from 'react-router-dom'
import Header from './Header/Header'
import style from './style.module.css'
import Footer from './Footer/Footer'
import Menu from '../Utils/Menu/Menu'
import Search from '../Utils/Search/Search'

function App() {
  const [isMenuVisible, setIsMenuVisible] = useState(false);
  const [isSearchVisible, setIsSearchVisible] = useState(false);

  return (
    <div className={ style.app }>
      <Header setIsMenuVisible={setIsMenuVisible} setIsSearchVisible={setIsSearchVisible} />
      { isMenuVisible ? <Menu setIsMenuVisible={setIsMenuVisible} /> : <></> }
      { isSearchVisible ? <Search setIsSearchVisible={setIsSearchVisible} /> : <></> }
      <Outlet />
      <Footer />
    </div>
  )
}

export default App