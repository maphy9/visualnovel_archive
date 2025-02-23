import React from 'react'
import logo from '../../../images/logo.png'
import homeIcon from '../../../images/homeIcon.png'
import discussionsIcon from '../../../images/dicussionsIcon.png'
import accountIcon from '../../../images/accountIcon.png'
import searchIcon from '../../../images/searchIcon.png'
import catalogIcon from '../../../images/catalogIcon.png'
import hamburgerIcon from '../../../images/hamburgerIcon.png'
import { Link } from 'react-router-dom'
import style from './style.module.css'

function Header({ setIsMenuVisible, setIsSearchVisible }) {
  return (
    <div className={style.header}>
      <div onClick={ () => setIsMenuVisible(true) } className={style.hamburger_button}>
        <img src={hamburgerIcon} alt="Hamburger icon" />
      </div>
      <Link to="/">
        <div className={style.header_logo}>
          <img src={logo} alt="VN Archive logo" />
        </div>
      </Link>
      <div className={style.header_navigation}>
        <Link id={style.hideable} to="/" className={style.header_button}>
          <div>
            <img src={homeIcon} alt='Home icon' />
            <p>Home</p>
          </div>
        </Link>
        <Link id={style.hideable} to="/visual_novels" className={style.header_button}>
          <div>
            <img src={catalogIcon} alt='Visual novels icon' />
            <p>Visual Novels</p>
          </div>
        </Link>
        <Link id={style.hideable} to="/discussions" className={style.header_button}>
          <div>
            <img src={discussionsIcon} alt='Discussions icon' />
            <p>Discussions</p>
          </div>
        </Link>
        <div style={{ cursor: "pointer" }} onClick={() => setIsSearchVisible(true) } className={style.header_button}>
          <div>
            <img src={searchIcon} alt='Search icon' />
            <p>Search</p>
          </div>
        </div>
        <Link id={style.hideable} to="/account" className={style.header_button}>
          <div>
            <img src={accountIcon} alt='Account icon' />
            <p>Account</p>
          </div>
        </Link>
      </div>
    </div>
  )
}

export default Header