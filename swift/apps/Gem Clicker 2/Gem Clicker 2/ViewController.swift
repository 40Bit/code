//
//  ViewController.swift
//  Gem Clicker 2
//
//  Created by Ayush on 4/13/19.
//  Copyright © 2019 Glinium. All rights reserved.
//

import UIKit

struct localStorage {
    static let gemsKey = "gems"
    static let drillInfoKey = "drillInfo"
    static let currentGemTypeKey = "currentGemType"
    static let nextGemTypeKey = "nextGemType"
    static let currentGemIndexKey = "currentGemIndex"
    static let gemsPerClickKey = "gemsPerClick"
}

let gemInfo = [
    "topaz": ["name": "Topaz", "cost": "0", "image": "Topaz.png"],
    "sapphire": ["name": "Sapphire", "cost": "1500", "image": "Sapphire.png"],
    "emerald": ["name": "Emerald", "cost": "5000", "image": "Emerald.png"],
    "ruby": ["name": "Ruby", "cost": "8000", "image": "Ruby.png"],
    "aquamarine": ["name": "Aquamarine", "cost": "15000", "image": "Aquamarine.png"],
    "diamond": ["name": "Diamond", "cost": "25500", "image": "Diamond.png"],
]

let defaults = UserDefaults.standard
let drillInfoDefault = ["drill": 0, "autoDrill": 0, "titaniumDrill": 0, "fireDrill": 0]
let currentGemTypeDefault = "topaz"
let nextGemTypeDefault = "sapphire"
let currentGemIndexDefault = 0
let gemOrder = ["topaz", "sapphire", "emerald", "ruby", "aquamarine", "diamond"]

var gemsPerClick = 1
var currentGemIndex = currentGemIndexDefault
var drillInfo = drillInfoDefault
var currentGemType = currentGemTypeDefault
var nextGemType = nextGemTypeDefault
var gems = 0

func startup() {
    gems = defaults.integer(forKey: localStorage.gemsKey)
    drillInfo = defaults.dictionary(forKey: localStorage.drillInfoKey) as? [String: Int] ?? drillInfoDefault
    currentGemType = defaults.string(forKey: localStorage.currentGemTypeKey) ?? currentGemTypeDefault
    nextGemType = defaults.string(forKey: localStorage.nextGemTypeKey) ?? nextGemTypeDefault
    currentGemIndex = defaults.integer(forKey: localStorage.currentGemIndexKey)
    gemsPerClick = defaults.integer(forKey: localStorage.gemsPerClickKey)
    if gemsPerClick == 0 {
        gemsPerClick = 1
    }
}

func main() {
    
    func store() {
        Canvas.shared.clear()
        
        let valuesNotTrueText = Text(string: "Not Enough Gems!", fontSize: 70.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        valuesNotTrueText.center.y = 0
        valuesNotTrueText.center.x -= 60
        
        let backText = Text(string: "Back", fontSize: 50.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        backText.center.y = 38
        backText.center.x = 25
        
        var buyGemText2 = Text(string: "Buy New Gem: ", fontSize: 60.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        buyGemText2.center.y = 30
        buyGemText2.center.x = 0
        
        var buyGemText = Text(string: (gemInfo[nextGemType]?["name"])! +
            " for " + (gemInfo[nextGemType]?["cost"])! + " gems", fontSize: 60.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        buyGemText.center.y = 25
        buyGemText.center.x = 0
        
        if currentGemType == "diamond" {
            buyGemText.center.y = 999
            buyGemText2.center.y = 999
        }
        
        let divider = Line(start: Point(x: 28, y: 19.3), end: Point(x: -28, y: 19.3))
        divider.color = #colorLiteral(red: 0.4745098054, green: 0.8392156959, blue: 0.9764705896, alpha: 1)
        
        var buyDrillText = Text(string: "Buy drill", fontSize: 51.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        buyDrillText.center.y = 14
        buyDrillText.center.x -= 21
        
        var buyAutoDrillText = Text(string: "Buy auto drill", fontSize: 51.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        buyAutoDrillText.center.y = 14
        buyAutoDrillText.center.x = 15
        
        buyGemText.onTouchUp {
            if gems > Int(gemInfo[currentGemType]!["cost"]!)! {
                currentGemIndex += 1
                currentGemType = gemOrder[currentGemIndex]
                nextGemType = gemOrder[currentGemIndex + 1]
                return
            } else {
                animate(duration: 0.7) {
                    
                }
                return
            }
        }
        
        backText.onTouchUp {
            defaults.set(drillInfo, forKey: localStorage.drillInfoKey)
            defaults.set(currentGemType, forKey: localStorage.currentGemTypeKey)
            defaults.set(nextGemType, forKey: localStorage.nextGemTypeKey)
            defaults.set(currentGemIndex, forKey: localStorage.currentGemIndexKey)
            defaults.set(gemsPerClick, forKey: localStorage.gemsPerClickKey)
            primary()
        }
    }
    
    func primary() {
        Canvas.shared.clear()
        
        Canvas.shared.color = Color.black
        var gem = Image(name: (gemInfo[currentGemType]?["image"])!)
        gem.size.width = 60
        gem.size.height = 60
        gem.center.x = 0
        gem.center.y -= 10
        
        var gemsText = Text(string: "Gems: " + String(gems), fontSize: 70.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        gemsText.center.y = 30
        gemsText.center.x = 0
        
        let storeText = Text(string: "Store", fontSize: 50.0, fontName: "Copperplate", color: #colorLiteral(red: 0.2392156869, green: 0.6745098233, blue: 0.9686274529, alpha: 1))
        storeText.center.y = 38
        storeText.center.x = 25
        
        storeText.onTouchUp {
            store()
        }
        
        gem.onTouchDown {
            gems += gemsPerClick
            gemsText.string = "Gems: " + String(gems)
            defaults.set(gems, forKey: localStorage.gemsKey)

        }
    }
    primary()
}

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        self.view = Canvas.shared.backingView
        startup()
        main()
    }

}
