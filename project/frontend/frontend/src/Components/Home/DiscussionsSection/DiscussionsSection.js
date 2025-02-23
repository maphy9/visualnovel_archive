import React from 'react'
import MainWindow from './MainWindow/MainWindow'
import SideWindow from './SideWindow/SideWindow'
import style from './style.module.css'

function DiscussionsSection() {
  return (
    <div className={style.section}>
      <MainWindow />
      <SideWindow />
    </div>
  )
}

export default DiscussionsSection