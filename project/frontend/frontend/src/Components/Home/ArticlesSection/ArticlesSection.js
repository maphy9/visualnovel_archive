import React from 'react'
import style from './style.module.css'
import MainWindow from './MainWindow/MainWindow'
import SideWindow from './SideWindow/SideWindow'

function ArticlesSection() {
  return (
    <div className={style.section}>
      <MainWindow />
      <SideWindow />
    </div>
  )
}

export default ArticlesSection