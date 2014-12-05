importClass(org.apache.commons.io.FileUtils);
importClass(java.io.File);

/*
 * Will try to use the power of Galen and Bash together to build up the workshop page out of the git tags
 */

function mandatorySystemProperty(name) {
    var value = System.getProperty(name);
    if (value != null) {
        return value;
    }
    else throw new Error("Missing System property: " + name);
}

var _workshopAllVersionsFolder = mandatorySystemProperty("workshop.all.versions");


var _devices = {
    mobile: {
        name: "mobile",
        size: "500x200",
        tags: "mobile"
    },
    tablet: {
        name: "tablet",
        size: "900x200",
        tags: "tablet"
    },
    desktop: {
        name: "desktop",
        size: "1300x200",
        tags: "desktop"
    }
};

test("Build website overview", function () {
    var driver = createDriver();

    var tagsText = readFile(_workshopAllVersionsFolder + "/git-tags");
    var lines = tagsText.split("\n");
    var versions = [];
    for (var i = 0; i < lines.length; i++) {
        var id = lines[i].indexOf(" ");
        var tagName = lines[i].substr(0, id);
        var tagDescription = lines[i].substr(id+1).trim();

        driver.get("file://" + _workshopAllVersionsFolder + "/" + tagName + "/website/shopping-cart.html");
        var version = {
            name: tagName,
            title: tagDescription,
            images: []
        };
        forAll(_devices, function (device) {
            resize(driver, device.size);
            var screenshotFile = takeScreenshot(driver);
            var fileName = "overview/screenshot-" + tagName + "-" + device.name + ".png";
            FileUtils.copyFile(screenshotFile, new File(_workshopAllVersionsFolder + "/" + fileName));
            version.images.push({
                device: device.name,
                image: fileName
            });

        });

        versions.push(version);
    }

    driver.quit();

    System.out.println("Generating HTML");

    var template = readFile("template/index.tpl.html");


    var html = template.replace("${middle}", generateOverviewLayout(versions));

    var file = new File(_workshopAllVersionsFolder + "/index.html");
    file.createNewFile();
    FileUtils.writeStringToFile(file, html);


    
});

function generateOverviewLayout(versions) {
    var html = "";
    for (var i = 0; i<versions.length; i++) {
        html +=
        "<div class='row container version'>\n \
            <div class='col-md-12 col-lg-12'><a class='github-tag' href='https://github.com/galenframework/workshop-shopping-cart/releases/tag/" + versions[i].name + "'>" + versions[i].name + "</a>\
            <a class='version-title' href='" + versions[i].name + "/website/shopping-cart.html'>" + versions[i].title + "</a> \
            </div>\
            <div class='col-md-4 col-lg-4'>\n \
                <h4>" + versions[i].images[0].device+ "</h4> \
                <img src='" + versions[i].images[0].image  + "'/> \
            </div>\n \
            <div class='col-md-4 col-lg-4'>\n \
                <h4>" + versions[i].images[1].device+ "</h4> \
                <img src='" + versions[i].images[1].image  + "'/> \
            </div>\n \
            <div class='col-md-4 col-lg-4'>\n \
                <h4>" + versions[i].images[2].device+ "</h4> \
                <img src='" + versions[i].images[2].image  + "'/> \
            </div>\n \
        </div>\n";
    }

    return html;
}







