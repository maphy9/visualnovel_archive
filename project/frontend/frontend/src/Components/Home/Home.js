import React from 'react'
import style from './style.module.css'
import ArticlesSection from './ArticlesSection/ArticlesSection'
import DiscussionsSection from './DiscussionsSection/DiscussionsSection'

function Home() {
  return (
    <div className={style.home}>
      <ArticlesSection />
      <DiscussionsSection />
    </div>
  )
}

export default Home