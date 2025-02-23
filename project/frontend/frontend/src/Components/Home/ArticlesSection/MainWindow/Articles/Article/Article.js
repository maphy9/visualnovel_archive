import React from 'react'
import style from './style.module.css'

function Article({ title, description, image }) {
  return (
    <div className={style.article}>
      <div className={style.article_text}>
        <div className={style.article_title}>{title}</div>
        <div className={style.article_description}>{description}</div>
      </div>
      <div className={style.article_image}>
        <img src={image} alt={`${title} image`} />
      </div>
    </div>
  )
}

export default Article