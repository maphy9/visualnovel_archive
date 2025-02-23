import React from 'react'
import style from './style.module.css'
import pageNotFound from '../../images/pageNotFound.jpg'

function NotFound() {
  return (
    <div className={style.notFound}>
      <b>Page not found ;-;</b>
      <img src={pageNotFound} alt="Page not found" />
      </div>
  )
}

export default NotFound