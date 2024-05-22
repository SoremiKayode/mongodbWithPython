my_data2 = [
    {"_id": 9787, "productTitle": 'Digital Camera DSLR', "price": 599.99, "sellerId": 'SELLER789', "sku": 'B07H57K575', "productUrl": 'https://example.com/images/camera.jpg', "uploadDate": '2024-03-10', "modify_date": '2024-03-31'},
    {"_id": 6568, "productTitle": 'Wireless Gaming Mouse', "price": 79.99, "sellerId": 'SELLER101', "sku": 'B089GJM2W5', "productUrl": 'https://example.com/images/mouse.jpg', "uploadDate": '2024-02-05', "modify_date": '2024-02-25'},
    {"_id": 5075, "productTitle": 'Portable Bluetooth Speaker', "price": 129.99, "sellerId": 'SELLER234', "sku": 'B07QK2SPP2', "productUrl": 'https://example.com/images/speaker.jpg', "uploadDate": '2024-01-20', "modify_date": '2024-02-10'},
    {"_id": 3688, "productTitle": 'Wireless Charging Pad', "price": 29.99, "sellerId": 'SELLER567', "sku": 'B07TZTGKB1', "productUrl": 'https://example.com/images/charging_pad.jpg', "uploadDate": '2024-02-10', "modify_date": '2024-03-02'},
    {"_id": 9533, "productTitle": 'Bluetooth Noise Cancelling Headphones', "price": 199.99, "sellerId": 'SELLER890', "sku": 'B07VRZKZ6G', "productUrl": 'https://example.com/images/headphones.jpg', "uploadDate": '2024-01-05', "modify_date": '2024-01-25'},
    {"_id": 2643, "productTitle": 'External Solid State Drive', "price": 179.99, "sellerId": 'SELLER112', "sku": 'B07YTG5R9D', "productUrl": 'https://example.com/images/ssd.jpg', "uploadDate": '2024-03-01', "modify_date": '2024-03-21'},
    {"_id": 3717, "productTitle": 'Wireless Security Camera', "price": 299.99, "sellerId": 'SELLER345', "sku": 'B08NYGGBPY', "productUrl": 'https://example.com/images/security_camera.jpg', "uploadDate": '2024-03-15', "modify_date": '2024-04-05'},
    {"_id": 8156, "productTitle": 'Wireless Mechanical Keyboard', "price": 129.99, "sellerId": 'SELLER678', "sku": 'B08CR6KN4Z', "productUrl": 'https://example.com/images/keyboard.jpg', "uploadDate": '2024-01-10', "modify_date": '2024-01-30'},
    {"_id": 1698, "productTitle": 'Smart Wi-Fi Thermostat', "price": 199.99, "sellerId": 'SELLER910', "sku": 'B07NX36KBW', "productUrl": 'https://example.com/images/thermostat.jpg', "uploadDate": '2024-02-20', "modify_date": '2024-03-12'},
    {"_id": 7285, "productTitle": 'Robot Vacuum Cleaner', "price": 349.99, "sellerId": 'SELLER123', "sku": 'B07QYDGD8Y', "productUrl": 'https://example.com/images/vacuum_cleaner.jpg', "uploadDate": '2024-02-15', "modify_date": '2024-03-06'},
    {"_id": 3426, "productTitle": 'Portable Power Bank', "price": 49.99, "sellerId": 'SELLER456', "sku": 'B07TWCSBZ2', "productUrl": 'https://example.com/images/power_bank.jpg', "uploadDate": '2024-03-05', "modify_date": '2024-03-25'},
    {"_id": 5314, "productTitle": 'Wireless Charging Stand', "price": 39.99, "sellerId": 'SELLER789', "sku": 'B07XQFNC98', "productUrl": 'https://example.com/images/charging_stand.jpg', "uploadDate": '2024-01-25', "modify_date": '2024-02-15'},
    {"_id": 4578, "productTitle": 'Bluetooth Car Stereo Receiver', "price": 69.99, "sellerId": 'SELLER101', "sku": 'B07WFSWZ29', "productUrl": 'https://example.com/images/car_stereo.jpg', "uploadDate": '2024-01-30', "modify_date": '2024-02-20'},
    {"_id": 2901, "productTitle": '4K Ultra HD Smart TV', "price": 899.99, "sellerId": 'SELLER234', "sku": 'B07PF1VKW2', "productUrl": 'https://example.com/images/smart_tv.jpg', "uploadDate": '2024-02-25', "modify_date": '2024-03-16'},
    {"_id": 6832, "productTitle": 'Wireless In-Ear Headphones', "price": 129.99, "sellerId": 'SELLER567', "sku": 'B08D94X6DK', "productUrl": 'https://example.com/images/in_ear_headphones.jpg', "uploadDate": '2024-01-01', "modify_date": '2024-01-21'},
    {"_id": 1743, "productTitle": 'Wi-Fi Mesh Router System', "price": 299.99, "sellerId": 'SELLER890', "sku": 'B07SPW8CSY', "productUrl": 'https://example.com/images/mesh_router.jpg', "uploadDate": '2024-03-20', "modify_date": '2024-04-10'},
    {"_id": 8197, "productTitle": 'Wireless Bluetooth Speaker', "price": 199.99, "sellerId": 'SELLER112', "sku": 'B08B5TYR26', "productUrl": 'https://example.com/images/bluetooth_speaker.jpg', "uploadDate": '2024-01-08', "modify_date": '2024-01-28'}
]

productImages = [
    {
        "_id": 9787,
        "sellerId": "SELLER789",
        "additionalImages": [
            "https://example.com/images/camera1.jpg",
            "https://example.com/images/camera2.jpg",
            "https://example.com/images/camera3.jpg"
        ],
        "uploadDate": "2024-03-10"
    },
    {
        "_id": 6568,
        "sellerId": "SELLER101",
        "additionalImages": [
            "https://example.com/images/mouse1.jpg",
            "https://example.com/images/mouse2.jpg",
            "https://example.com/images/mouse3.jpg"
        ],
        "uploadDate": "2024-02-05"
    },
    {
        "_id": 5075,
        "sellerId": "SELLER234",
        "additionalImages": [
            "https://example.com/images/speaker1.jpg",
            "https://example.com/images/speaker2.jpg",
            "https://example.com/images/speaker3.jpg"
        ],
        "uploadDate": "2024-01-20"
    },
    {
        "_id": 3688,
        "sellerId": "SELLER567",
        "additionalImages": [
            "https://example.com/images/charging_pad1.jpg",
            "https://example.com/images/charging_pad2.jpg",
            "https://example.com/images/charging_pad3.jpg"
        ],
        "uploadDate": "2024-02-10"
    },
    {
        "_id": 9533,
        "sellerId": "SELLER890",
        "additionalImages": [
            "https://example.com/images/headphones1.jpg",
            "https://example.com/images/headphones2.jpg",
            "https://example.com/images/headphones3.jpg"
        ],
        "uploadDate": "2024-01-05"
    },
    {
        "_id": 2643,
        "sellerId": "SELLER112",
        "additionalImages": [
            "https://example.com/images/ssd1.jpg",
            "https://example.com/images/ssd2.jpg",
            "https://example.com/images/ssd3.jpg"
        ],
        "uploadDate": "2024-03-01"
    },
    {
        "_id": 3717,
        "sellerId": "SELLER345",
        "additionalImages": [
            "https://example.com/images/security_camera1.jpg",
            "https://example.com/images/security_camera2.jpg",
            "https://example.com/images/security_camera3.jpg"
        ],
        "uploadDate": "2024-03-15"
    },
    {
        "_id": 8156,
        "sellerId": "SELLER678",
        "additionalImages": [
            "https://example.com/images/keyboard1.jpg",
            "https://example.com/images/keyboard2.jpg",
            "https://example.com/images/keyboard3.jpg"
        ],
        "uploadDate": "2024-01-10"
    },
    {
        "_id": 1698,
        "sellerId": "SELLER910",
        "additionalImages": [
            "https://example.com/images/thermostat1.jpg",
            "https://example.com/images/thermostat2.jpg",
            "https://example.com/images/thermostat3.jpg"
        ],
        "uploadDate": "2024-02-20"
    },
    {
        "_id": 7285,
        "sellerId": "SELLER123",
        "additionalImages": [
            "https://example.com/images/vacuum_cleaner1.jpg",
            "https://example.com/images/vacuum_cleaner2.jpg",
            "https://example.com/images/vacuum_cleaner3.jpg"
        ],
        "uploadDate": "2024-02-15"
    },
    {
        "_id": 3426,
        "sellerId": "SELLER456",
        "additionalImages": [
            "https://example.com/images/power_bank1.jpg",
            "https://example.com/images/power_bank2.jpg",
            "https://example.com/images/power_bank3.jpg"
        ],
        "uploadDate": "2024-03-05"
    },
    {
        "_id": 5314,
        "sellerId": "SELLER789",
        "additionalImages": [
            "https://example.com/images/charging_stand1.jpg",
            "https://example.com/images/charging_stand2.jpg",
            "https://example.com/images/charging_stand3.jpg"
        ],
        "uploadDate": "2024-01-25"
    },
    {
        "_id": 4578,
        "sellerId": "SELLER101",
        "additionalImages": [
            "https://example.com/images/car_stereo1.jpg",
            "https://example.com/images/car_stereo2.jpg",
            "https://example.com/images/car_stereo3.jpg"
        ],
        "uploadDate": "2024-01-30"
    },
    {
        "_id": 2901,
        "sellerId": "SELLER234",
        "additionalImages": [
            "https://example.com/images/smart_tv1.jpg",
            "https://example.com/images/smart_tv2.jpg",
            "https://example.com/images/smart_tv3.jpg"
        ],
        "uploadDate": "2024-02-25"
    },
    {
        "_id": 6832,
        "sellerId": "SELLER567",
        "additionalImages": [
            "https://example.com/images/in_ear_headphones1.jpg",
            "https://example.com/images/in_ear_headphones2.jpg",
            "https://example.com/images/in_ear_headphones3.jpg"
        ],
        "uploadDate": "2024-01-01"
    },
    {
        "_id": 1743,
        "sellerId": "SELLER890",
        "additionalImages": [
            "https://example.com/images/mesh_router1.jpg",
            "https://example.com/images/mesh_router2.jpg",
            "https://example.com/images/mesh_router3.jpg"
        ],
        "uploadDate": "2024-03-20"
    },
    {
        "_id": 8197,
        "sellerId": "SELLER112",
        "additionalImages": [
            "https://example.com/images/bluetooth_speaker1.jpg",
            "https://example.com/images/bluetooth_speaker2.jpg",
            "https://example.com/images/bluetooth_speaker3.jpg"
        ],
        "uploadDate": "2024-01-08"
    }
]

sales_details = [
    {
        "product_id": 9787,
        "buyerId": "BUYER001",
        "dateOfPurchase": "2024-03-15",
        "QuantityPurchase": 1,
        "shippingAddress": "123 Main St, Springfield, IL"
    },
    {
        "product_id": 6568,
        "buyerId": "BUYER002",
        "dateOfPurchase": "2024-02-10",
        "QuantityPurchase": 2,
        "shippingAddress": "456 Elm St, Denver, CO"
    },
    {
        "product_id": 5075,
        "buyerId": "BUYER003",
        "dateOfPurchase": "2024-01-25",
        "QuantityPurchase": 1,
        "shippingAddress": "789 Oak St, Austin, TX"
    },
    {
        "product_id": 3688,
        "buyerId": "BUYER004",
        "dateOfPurchase": "2024-02-12",
        "QuantityPurchase": 3,
        "shippingAddress": "101 Maple St, Seattle, WA"
    },
    {
        "product_id": 9533,
        "buyerId": "BUYER005",
        "dateOfPurchase": "2024-01-10",
        "QuantityPurchase": 1,
        "shippingAddress": "202 Pine St, Boston, MA"
    },
    {
        "product_id": 2643,
        "buyerId": "BUYER006",
        "dateOfPurchase": "2024-03-05",
        "QuantityPurchase": 1,
        "shippingAddress": "303 Cedar St, Miami, FL"
    },
    {
        "product_id": 3717,
        "buyerId": "BUYER007",
        "dateOfPurchase": "2024-03-18",
        "QuantityPurchase": 2,
        "shippingAddress": "404 Birch St, Portland, OR"
    },
    {
        "product_id": 8156,
        "buyerId": "BUYER008",
        "dateOfPurchase": "2024-01-15",
        "QuantityPurchase": 1,
        "shippingAddress": "505 Walnut St, Chicago, IL"
    },
    {
        "product_id": 1698,
        "buyerId": "BUYER009",
        "dateOfPurchase": "2024-02-25",
        "QuantityPurchase": 1,
        "shippingAddress": "606 Spruce St, San Francisco, CA"
    },
    {
        "product_id": 7285,
        "buyerId": "BUYER010",
        "dateOfPurchase": "2024-02-20",
        "QuantityPurchase": 1,
        "shippingAddress": "707 Willow St, New York, NY"
    },
    {
        "product_id": 3426,
        "buyerId": "BUYER011",
        "dateOfPurchase": "2024-03-10",
        "QuantityPurchase": 1,
        "shippingAddress": "808 Cherry St, Houston, TX"
    },
    {
        "product_id": 5314,
        "buyerId": "BUYER012",
        "dateOfPurchase": "2024-01-28",
        "QuantityPurchase": 1,
        "shippingAddress": "909 Ash St, Atlanta, GA"
    },
    {
        "product_id": 4578,
        "buyerId": "BUYER013",
        "dateOfPurchase": "2024-02-02",
        "QuantityPurchase": 1,
        "shippingAddress": "1010 Poplar St, Dallas, TX"
    },
    {
        "product_id": 2901,
        "buyerId": "BUYER014",
        "dateOfPurchase": "2024-03-01",
        "QuantityPurchase": 1,
        "shippingAddress": "1111 Chestnut St, Las Vegas, NV"
    },
    {
        "product_id": 6832,
        "buyerId": "BUYER015",
        "dateOfPurchase": "2024-01-05",
        "QuantityPurchase": 2,
        "shippingAddress": "1212 Pine St, Orlando, FL"
    },
    {
        "product_id": 1743,
        "buyerId": "BUYER016",
        "dateOfPurchase": "2024-03-25",
        "QuantityPurchase": 1,
        "shippingAddress": "1313 Cedar St, San Diego, CA"
    },
    {
        "product_id": 8197,
        "buyerId": "BUYER017",
        "dateOfPurchase": "2024-01-12",
        "QuantityPurchase": 1,
        "shippingAddress": "1414 Birch St, Phoenix, AZ"
    },
        {
        "product_id": 8197,
        "buyerId": "BUYER017",
        "dateOfPurchase": "2024-01-12",
        "QuantityPurchase": 1,
        "shippingAddress": "1414 Birch St, Phoenix, AZ"
    },
    {
        "product_id": 1743,
        "buyerId": "BUYER018",
        "dateOfPurchase": "2024-04-01",
        "QuantityPurchase": 1,
        "shippingAddress": "1515 Maple St, Denver, CO"
    },
    {
        "product_id": 6832,
        "buyerId": "BUYER019",
        "dateOfPurchase": "2024-01-10",
        "QuantityPurchase": 3,
        "shippingAddress": "1616 Walnut St, Austin, TX"
    },
    {
        "product_id": 2901,
        "buyerId": "BUYER020",
        "dateOfPurchase": "2024-03-05",
        "QuantityPurchase": 2,
        "shippingAddress": "1717 Pine St, Miami, FL"
    },
    {
        "product_id": 4578,
        "buyerId": "BUYER021",
        "dateOfPurchase": "2024-02-15",
        "QuantityPurchase": 1,
        "shippingAddress": "1818 Cedar St, Portland, OR"
    },
    {
        "product_id": 5314,
        "buyerId": "BUYER022",
        "dateOfPurchase": "2024-01-30",
        "QuantityPurchase": 1,
        "shippingAddress": "1919 Birch St, Chicago, IL"
    },
    {
        "product_id": 3426,
        "buyerId": "BUYER023",
        "dateOfPurchase": "2024-03-15",
        "QuantityPurchase": 1,
        "shippingAddress": "2020 Spruce St, San Francisco, CA"
    },
    {
        "product_id": 7285,
        "buyerId": "BUYER024",
        "dateOfPurchase": "2024-02-22",
        "QuantityPurchase": 1,
        "shippingAddress": "2121 Willow St, New York, NY"
    },
    {
        "product_id": 1698,
        "buyerId": "BUYER025",
        "dateOfPurchase": "2024-03-01",
        "QuantityPurchase": 1,
        "shippingAddress": "2222 Cherry St, Houston, TX"
    },
    {
        "product_id": 8156,
        "buyerId": "BUYER026",
        "dateOfPurchase": "2024-01-20",
        "QuantityPurchase": 1,
        "shippingAddress": "2323 Ash St, Atlanta, GA"
    },
    {
        "product_id": 3717,
        "buyerId": "BUYER027",
        "dateOfPurchase": "2024-03-20",
        "QuantityPurchase": 1,
        "shippingAddress": "2424 Poplar St, Dallas, TX"
    },
    {
        "product_id": 2643,
        "buyerId": "BUYER028",
        "dateOfPurchase": "2024-03-10",
        "QuantityPurchase": 1,
        "shippingAddress": "2525 Chestnut St, Las Vegas, NV"
    },
    {
        "product_id": 9533,
        "buyerId": "BUYER029",
        "dateOfPurchase": "2024-01-12",
        "QuantityPurchase": 1,
        "shippingAddress": "2626 Pine St, Orlando, FL"
    },
    {
        "product_id": 3688,
        "buyerId": "BUYER030",
        "dateOfPurchase": "2024-02-20",
        "QuantityPurchase": 1,
        "shippingAddress": "2727 Cedar St, San Diego, CA"
    },
    {
        "product_id": 5075,
        "buyerId": "BUYER031",
        "dateOfPurchase": "2024-01-30",
        "QuantityPurchase": 1,
        "shippingAddress": "2828 Birch St, Phoenix, AZ"
    },
    {
        "product_id": 6568,
        "buyerId": "BUYER032",
        "dateOfPurchase": "2024-02-15",
        "QuantityPurchase": 1,
        "shippingAddress": "2929 Maple St, Denver, CO"
    },
    {
        "product_id": 9787,
        "buyerId": "BUYER033",
        "dateOfPurchase": "2024-03-18",
        "QuantityPurchase": 1,
        "shippingAddress": "3030 Walnut St, Austin, TX"
    }
]

