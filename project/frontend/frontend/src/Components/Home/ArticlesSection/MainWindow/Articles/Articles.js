import React from 'react'
import style from './style.module.css'
import Article from './Article/Article'

function Articles({ articles }) {
  const elements = articles.map((article, index) => <Article key={index} title={article.title} description={article.description} image={article.image} />);
  return (
    <div className={style.articles}>{elements}</div>
  )
}

export default Articles