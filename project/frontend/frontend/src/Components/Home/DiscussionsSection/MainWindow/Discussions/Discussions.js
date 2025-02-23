import React from 'react'
import style from './style.module.css'
import Discussion from './Discussion/Discussion'

function Discussions({ discussions }) {
  const elements = discussions.map((discussion, index) => <Discussion key={index} title={discussion.title} description={discussion.description} image={discussion.image} />);
  return (
    <div className={style.discussions}>{elements}</div>
  )
}

export default Discussions