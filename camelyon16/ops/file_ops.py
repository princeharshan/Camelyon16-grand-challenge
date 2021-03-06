import os
from shutil import copyfile
import random
import sys
import glob
import camelyon16.utils as utils


def copy_all(from_dir, to_dir, file_names, name_pattern):

    if name_pattern is not None:
        print('moving files with pattern: %s' % name_pattern)
        file_paths = glob.glob(os.path.join(from_dir, name_pattern))
        total_file_count = len(file_paths)
        print('Files found: %d' % total_file_count)
        for index in range(total_file_count):
            copyfile(file_paths[index], to_dir + utils.get_filename_from_path(file_paths[index]))
            if not index % 1000:
                print('moved %d of %d files.' % (index, total_file_count))
                sys.stdout.flush()
    else:
        total_file_count = len(file_names)
        print('copying all files: %d' % total_file_count)
        for index in range(total_file_count):
            copyfile(from_dir + file_names[index], to_dir + file_names[index])
            if not index % 1000:
                print('copied %d of %d files.' % (index, total_file_count))
                sys.stdout.flush()


def copy_files(from_dir, to_dir, name_pattern=None, n_sample=None):
    print('copy_files() - From: %s' % from_dir)
    print('copy_files() -   To: %s' % to_dir)
    file_names = os.listdir(from_dir)
    file_names = sorted(file_names)
    if n_sample is None:
        copy_all(from_dir, to_dir, file_names, name_pattern)
    else:
        assert len(file_names) >= n_sample, "Not enough files to copy. available: %d, requested: %d" % \
                                           (len(file_names), n_sample)

        if name_pattern is None:
            shuffled_index = list(range(len(file_names)))
            random.seed(12345)
            random.shuffle(shuffled_index)
            for index in range(n_sample):
                copyfile(from_dir + file_names[shuffled_index[index]], to_dir + file_names[shuffled_index[index]])
                if not index % 1000:
                    print('copied %d of %d files.' % (index, n_sample))
                    sys.stdout.flush()
        else:
            print('copying files with pattern: %s' % name_pattern)
            file_paths = glob.glob(os.path.join(from_dir, name_pattern))
            total_file_count = len(file_paths)
            print('Files found: %d' % total_file_count)
            assert len(file_paths) >= n_sample, "Not enough files to copy with requested pattern. available: %d, " \
                                                "requested: %d" % (total_file_count, n_sample)
            file_paths = file_paths[:n_sample]
            for index in range(n_sample):
                copyfile(file_paths[index], to_dir + utils.get_filename_from_path(file_paths[index]))
                if not index % 1000:
                    print('copied %d of %d files.' % (index, n_sample))
                    sys.stdout.flush()


def move_all(from_dir, to_dir, file_names, name_pattern):

    if name_pattern is not None:
        print('moving files with pattern: %s' % name_pattern)
        file_paths = glob.glob(os.path.join(from_dir, name_pattern))
        total_file_count = len(file_paths)
        print('Files found: %d' % total_file_count)
        for index in range(total_file_count):
            os.rename(file_paths[index], to_dir + utils.get_filename_from_path(file_paths[index]))
            if not index % 1000:
                print('moved %d of %d files.' % (index, total_file_count))
                sys.stdout.flush()
    else:
        total_file_count = len(file_names)
        print('moving all files: %d' % total_file_count)
        for index in range(total_file_count):
            os.rename(from_dir + file_names[index], to_dir + file_names[index])
            if not index % 1000:
                print('moved %d of %d files.' % (index, total_file_count))
                sys.stdout.flush()


def move_files(from_dir, to_dir, name_pattern=None, n_sample=None):
    print('move_files() - From: %s' % from_dir)
    print('move_files() -   To: %s' % to_dir)
    file_names = os.listdir(from_dir)
    file_names = sorted(file_names)
    if n_sample is None:
        move_all(from_dir, to_dir, file_names, name_pattern)
    else:
        assert len(file_names) >= n_sample, "Not enough files to move. available: %d, requested: %d" % \
                                           (len(file_names), n_sample)
        if name_pattern is None:
            shuffled_index = list(range(len(file_names)))
            random.seed(12345)
            random.shuffle(shuffled_index)
            # print(sorted(shuffled_index[:n_sample]))
            for index in range(n_sample):
                os.rename(from_dir + file_names[shuffled_index[index]], to_dir + file_names[shuffled_index[index]])
                if not index % 1000:
                    print('moved %d of %d files.' % (index, n_sample))
                    sys.stdout.flush()
        else:
            print('moving files with pattern: %s' % name_pattern)
            file_paths = glob.glob(os.path.join(from_dir, name_pattern))
            total_file_count = len(file_paths)
            print('Files found: %d' % total_file_count)
            assert len(file_paths) >= n_sample, "Not enough files to move with requested pattern. available: %d, " \
                                                "requested: %d" % (total_file_count, n_sample)
            file_paths = file_paths[:n_sample]
            for index in range(n_sample):
                os.rename(file_paths[index], to_dir + utils.get_filename_from_path(file_paths[index]))
                if not index % 1000:
                    print('moved %d of %d files.' % (index, n_sample))
                    sys.stdout.flush()


def delete_all(from_dir, file_names, name_pattern):

    if name_pattern is not None:
        print('deleting files with pattern: %s' % name_pattern)
        file_paths = glob.glob(os.path.join(from_dir, name_pattern))
        total_file_count = len(file_paths)
        print('Files found: %d' % total_file_count)
        for index in range(total_file_count):
            os.remove(file_paths[index])
            if not index % 1000:
                print('deleted %d of %d files.' % (index, total_file_count))
                sys.stdout.flush()
    else:
        total_file_count = len(file_names)
        print('deleting all files : %d' % total_file_count)
        for index in range(total_file_count):
            os.remove(from_dir + file_names[index])
            if not index % 1000:
                print('deleted %d of %d files.' % (index, total_file_count))
                sys.stdout.flush()


def delete_files(from_dir, name_pattern=None, n_sample=None):
    print('delete_files() - From: %s' % from_dir)
    file_names = os.listdir(from_dir)
    file_names = sorted(file_names)
    if n_sample is None:
        delete_all(from_dir, file_names, name_pattern)
    else:
        assert len(file_names) >= n_sample, "Not enough files to delete. available: %d, requested: %d" % \
                                            (len(file_names), n_sample)
        if name_pattern is None:
            shuffled_index = list(range(len(file_names)))
            random.seed(12345)
            random.shuffle(shuffled_index)
            for index in range(n_sample):
                os.remove(from_dir + file_names[shuffled_index[index]])
                if not index % 1000:
                    print('deleted %d of %d files.' % (index, n_sample))
                    sys.stdout.flush()
        else:
            print('deleting files with pattern: %s' % name_pattern)
            file_paths = glob.glob(os.path.join(from_dir, name_pattern))
            total_file_count = len(file_paths)
            print('Files found: %d' % total_file_count)
            assert len(file_paths) >= n_sample, "Not enough files to delete with requested pattern. available: %d, " \
                                                "requested: %d" % (total_file_count, n_sample)
            file_paths = file_paths[:n_sample]
            for index in range(n_sample):
                os.remove(file_paths[index])
                if not index % 1000:
                    print('deleted %d of %d files.' % (index, n_sample))
                    sys.stdout.flush()


def search(search_dir, name_pattern='*'):
    file_paths = glob.glob(os.path.join(search_dir, name_pattern))
    print("Found %d files with pattern '%s' into '%s'." % (len(file_paths), name_pattern, search_dir))


def perform_ops():
    print()
    # copy_files(utils.PATCHES_TRAIN_AUG_NEGATIVE_PATH, utils.PATCHES_TRAIN_NEGATIVE_PATH)
    # delete_files(utils.PATCHES_VALIDATION_NEGATIVE_PATH)
    # delete_files(utils.PATCHES_TRAIN_NEGATIVE_PATH, 'normal_*', n_sample=7381)
    # move_files(utils.PATCHES_TRAIN_NEGATIVE_PATH, utils.PATCHES_VALIDATION_NEGATIVE_PATH, n_sample=5000)
    # delete_files(utils.PATCHES_TRAIN_NEGATIVE_PATH, 'aug_false_normal*')
    # search(utils.PATCHES_VALIDATION_NEGATIVE_PATH, 'aug_false_normal*')
    # move_files(utils.PATCHES_TRAIN_NEGATIVE_PATH, utils.PATCHES_VALIDATION_NEGATIVE_PATH,
    #            name_pattern='aug_false_normal*', n_sample=250)
    # move_files(utils.PATCHES_TRAIN_POSITIVE_PATH, utils.PATCHES_VALIDATION_POSITIVE_PATH,
    #            name_pattern='aug_false_tumor*', n_sample=46)
    # delete_files(utils.PATCHES_VALIDATION_NEGATIVE_PATH, 'normal_*', 476)
    search(utils.PATCHES_TRAIN_NEGATIVE_PATH, 'normal_*')
    delete_files(utils.PATCHES_TRAIN_NEGATIVE_PATH, 'normal_*', 2182)

if __name__ == '__main__':
    perform_ops()
