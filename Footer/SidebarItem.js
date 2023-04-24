import React from 'react'
import "../../styles/Sidebar.css"
import ArrowRightIcon from '@material-ui/icons/ArrowRight';

function SidebarItem( { arrow, icon, label, active }) {
    return (
        <div className={active ? "sidebarItem active" : "sidebarItem"}>
            <div className="sidebarItem__arrow">
                {arrow && ( <ArrowRightIcon /> )}
            </div>

            <div className="sidebarItem__main">
                {icon}
                <p className={active ? "sidebarItem__heading" : ""}>{label}</p>
            </div>
        </div>
    )
}

export default SidebarItem
