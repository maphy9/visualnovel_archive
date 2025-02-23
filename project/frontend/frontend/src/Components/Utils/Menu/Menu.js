import React, { useEffect, useState } from 'react'
import style from './style.module.css'
import homeIcon from '../../../images/homeIcon.png'
import discussionsIcon from '../../../images/dicussionsIcon.png'
import accountIcon from '../../../images/accountIcon.png'
import closeIcon from '../../../images/closeIcon.png'
import catalogIcon from '../../../images/catalogIcon.png'
import { Link } from 'react-router-dom'

function Menu({ setIsMenuVisible }) {
  const [height, setHeight] = useState('');
  useEffect(() => {
    const updateHeight = () => {
      setHeight(`${document.documentElement.scrollHeight}px`);
    };
    updateHeight();
    window.addEventListener('resize', updateHeight);
    return () => window.removeEventListener('resize', updateHeight);
  }, []);

  return (
    <>
      <div className={style.blurBackground} style={{ height }}></div>
      <div className={style.menu}>
        <div class={style.close}><img onClick={ () => setIsMenuVisible(false) } src={closeIcon} alt="Close" /></div>
        <Link to="/" className={style.item}>
          <div>
            <img src={homeIcon} alt='Home icon' />
            <p>Home</p>
          </div>
        </Link>
        <Link to="/visual_novels" className={style.item}>
          <div>
            <img src={catalogIcon} alt='Visual novels icon' />
            Visual Novels
          </div>
        </Link>
        <Link  to="/discussions" className={style.item}>
          <div>
            <img src={discussionsIcon} alt='Discussions icon' />
            <p>Discussions</p>
          </div>
        </Link>
        <Link to="/account" className={style.item}>
          <div>
            <img src={accountIcon} alt='Account icon' />
            <p>Account</p>
          </div>
        </Link>
      </div>
    </>
  )
}

export default Menu