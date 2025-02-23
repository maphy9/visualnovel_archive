import React from 'react'
import style from './style.module.css'
import defaultUserProfilePicture from '../../../../../../images/defaultUserProfilePicture.png'

function User({ username, image, role, ranking, joined }) {
  return (
    <div className={style.user}>
      <div className={style.image}>
        <img src={image !== null ? image : defaultUserProfilePicture} alt={`${username} profile picture`} />
      </div>
      <div className={style.data}>
        <div className={style.text}>
          <div className={style.username}>{username}</div>
          <div className={style.ranking}>Ranking: <b>{ranking}</b></div>
        </div>
        <div className={style.text}>
          <div className={style.role}>{role}</div>
          <div className={style.joined}>Joined: {joined}</div>
        </div>
      </div>
    </div>
  )
}

export default User