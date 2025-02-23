import React from 'react'
import style from './style.module.css'

function Result({ title, image }) {
  return (
    <div className={style.result}>
      <div className={style.title}>{title}</div>
      <div className={style.image}>
        <img src={image} alt={`${title} image`} />
      </div>
    </div>
  )
}

export default Result