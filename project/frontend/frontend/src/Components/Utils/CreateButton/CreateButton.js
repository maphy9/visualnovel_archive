import React from 'react'
import style from './style.module.css'
import { Link } from 'react-router-dom'
import createIcon from '../../../images/createIcon.png'

function CreateButton({ url, label }) {
  return (
    <Link to={url}>
      <div className={style.button}>
        <img src={createIcon} alt="Create icon" />
        <div>{label}</div>
      </div>
    </Link>
  )
}

export default CreateButton