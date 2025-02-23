import React from 'react'
import style from './style.module.css'

function Discussion({ title, description, image }) {
  return (
    <div className={style.discussion}>
      <div className={style.discussion_text}>
        <div className={style.discussion_title}>{title}</div>
        <div className={style.discussion_description}>{description}</div>
      </div>
      <div className={style.discussion_image}>
        <img src={image} alt={`${title} image`} />
      </div>
    </div>
  )
}

export default Discussion