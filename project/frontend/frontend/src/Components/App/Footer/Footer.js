import React from 'react'
import style from './style.module.css'
import { Link } from 'react-router-dom'

function Footer() {
  return (
    <div className={style.footer}>
        <Link to="/privacy_policy">Privacy policy</Link>
        <Link to="/about">About VN Archive</Link>
    </div>
  )
}

export default Footer