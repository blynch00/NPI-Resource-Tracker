//import { useState } from "react";
import './SavedTable.css'
export const SavedTable = () => {
    
    const users =[
  {
    "npi_code": "1679576722",
    "last_name": "WIEBE",
    "first_name": "DAVID",
    "address_1": "PO BOX 2168",
    "address_2": "XX",
    "city": "KEARNEY",
    "state": "NE",
    "zip": "688482168",
    "phone": "3088652512",
    "taxonomy_code": "207X00000X"
  },
  {
    "npi_code": "1588667638",
    "last_name": "PILCHER",
    "first_name": "WILLIAM",
    "address_1": "1824 KING STREET",
    "address_2": "SUITE 300",
    "city": "JACKSONVILLE",
    "state": "FL",
    "zip": "322044736",
    "phone": "9043881820",
    "taxonomy_code": "207RC0000X"
  },
  {
    "npi_code": "1497758544",
    "last_name": "XX",
    "first_name": "XX",
    "address_1": "3418 VILLAGE DR",
    "address_2": "XX",
    "city": "FAYETTEVILLE",
    "state": "NC",
    "zip": "283044552",
    "phone": "9106096740",
    "taxonomy_code": "251G00000X"
  },
  {
    "npi_code": "1306849450",
    "last_name": "XX",
    "first_name": "XX",
    "address_1": "XX",
    "address_2": "XX",
    "city": "XXXXX",
    "state": "XX",
    "zip": "XXXXX",
    "phone": "XXXXXXXXXX",
    "taxonomy_code": "XXXXXXXXXX"
  },
  {
    "npi_code": "1215930367",
    "last_name": "GRESSOT",
    "first_name": "LAURENT",
    "address_1": "17323 RED OAK DR",
    "address_2": "XX",
    "city": "HOUSTON",
    "state": "TX",
    "zip": "770901243",
    "phone": "2814405006",
    "taxonomy_code": "174400000X"
  },
  {
    "npi_code": "1023011178",
    "last_name": "XX",
    "first_name": "XX",
    "address_1": "414 S JEFFERSON ST",
    "address_2": "XX",
    "city": "NAPA",
    "state": "CA",
    "zip": "945594515",
    "phone": "7072589080",
    "taxonomy_code": "251G00000X"
  },
  {
    "npi_code": "1932102084",
    "last_name": "ADUSUMILLI",
    "first_name": "RAVI",
    "address_1": "2940 N MCCORD RD",
    "address_2": "XX",
    "city": "TOLEDO",
    "state": "OH",
    "zip": "436151753",
    "phone": "4198423000",
    "taxonomy_code": "207RC0000X"
  }
    ];

    return (
        <div className="overflow-x-auto">
            <table>
                <thead>
                    <tr>
                        <th>NPI Code</th>
                        <th>Last Name</th>
                        <th>First Name</th>
                        <th>Address</th>
                        <th>Address 2</th>
                        <th>City</th>
                        <th>State</th>
                        <th>Zip</th>
                        <th>Phone</th>
                        <th>Zip Code</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map((user, index) => (
                        <tr key={index}>
                            <td>{user.npi_code}</td>
                            <td>{user.last_name}</td>
                            <td>{user.first_name}</td>
                            <td>{user.address_1}</td>
                            <td>{user.address_2}</td>
                            <td>{user.city}</td>
                            <td>{user.state}</td>
                            <td>{user.zip}</td>
                            <td>{user.phone}</td>
                            <td>{user.taxonomy_code}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
};

