import UIKit
// import PlaygroundSupport

public func _setup() {
    let viewController = UIViewController()
    viewController.view = Canvas.shared.backingView
    viewController.preferredContentSize = CGSize(width: 800, height: 700)
    // PlaygroundPage.current.liveView = viewController
}
